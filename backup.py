import os
from pickleSavefiles import SaveFiles
from datetime import datetime
from constants.directories import Directory, Filenames, FilenameToSheet, FilenameToPath
from constants.googleSheet import SheetName, SheetColumnCampainNum
from campain import PokeCommands
from sheetInfo import SheetCommands
from pokemon import Pokemon

class Backup:
    
    @staticmethod
    def create():
            '''Create backup from .pkl savefiles. [[datetime], [players], [wild pokemon], [npcs], [gym leaders]]'''
            dt = datetime.now()
            print("Backing up files:", dt)
            backup = []
            backup.append(dt)
            poke_players = SaveFiles.openFile(Directory.PLAYERS)
            backup.append(poke_players)
            poke_wild = SaveFiles.openFile(Directory.WILD_POKEMON)
            backup.append(poke_wild)
            poke_npcs = SaveFiles.openFile(Directory.NPCS)
            backup.append(poke_npcs)
            poke_gym = SaveFiles.openFile(Directory.LEADERS_GEN4)
            backup.append(poke_gym)
            
            path = os.path.join(Directory.BACKUPS, dt.strftime('%Y-%m-%d_%H-%M-%S')+'.pkl')
            temp = open(path, 'wb')
            temp.close()
            SaveFiles.savePokemon(backup, path)

    @staticmethod
    def show():
        '''Show all backups'''
        i=1
        buckupsName = os.listdir(Directory.BACKUPS)
        
        for backup in buckupsName:
            print('Back up [',i,']: ', backup, sep='')
            i=i+1      

    @staticmethod
    def get(index = 0, filename="") -> tuple[list[datetime], list[Pokemon], list[Pokemon], list[Pokemon], list[Pokemon]]:
        '''Returns backup from index (default) or filename. 0 to get latest backup.\n
        [[datetime], [players], [wild pokemon], [npcs], [gym leaders]]'''
        try:
            if filename == "":
                backupsname = os.listdir(Directory.BACKUPS)
                backup = SaveFiles.openFile(os.path.join(Directory.BACKUPS, backupsname[index-1]))
            else:
                backup = SaveFiles.openFile(os.path.join(Directory.BACKUPS, filename))
            return backup
        except Exception as e:
            print("Error in getting backup:", e)
            return None
        
    @staticmethod
    def deleteRange(num:int):
        '''Delete range from backups, starting from oldest. 0 to delete all backups'''
        backupsname = os.listdir(Directory.BACKUPS)
        if num == 0:
            print("Deleting all backups. Do you want to proceed?\n(Y/n)")
            if input().lower() != 'y': return None
            for i in range(len(backupsname)):
                os.remove(os.path.join(Directory.BACKUPS, backupsname[i]))
            print("Successfully deleted all backups!")
        elif num > 0 and num <= len(backupsname):
            print("Deleting",num, "oldest backup(s). Do you want to proceed?\n(Y/n)")
            if input().lower() != 'y': return None
            for i in range(num):
                os.remove(os.path.join(Directory.BACKUPS, backupsname[i]))
            print("Successfully deleted backups!")
        else: print("Invalid range")
    
    @staticmethod
    def delete(index = 0, filename = ""):
        '''Delete backup from index (default) or filename'''
        backupsname = os.listdir(Directory.BACKUPS)
        if filename == "": bname = backupsname[index-1]
        else: bname = filename
        print("Deleting backup [ {backup} ]. Do you want to proceed?\n(Y/n)".format(bname))
        if input().lower() != 'y': return None
        os.remove(os.path.join(Directory.BACKUPS, bname))
    
    @staticmethod
    def rollback(index:int):
        '''Replaces most recent backup with backup from index'''
        backupNew = Backup.get(index)
        print("Rolling back savefiles from", backupNew[0],
              "\nWould you like to create backup of current files before overwriting?")
        ans = input("(Y/n)\n")
        if ans.lower() == 'y':
            Backup.create()
        
        backupOld = Backup.get(-1)
        dt = datetime(backupOld[0])
        backupOld = backupNew
        backupOld[0] = dt
        
        path = os.path.join(Directory.BACKUPS, dt.strftime('%Y-%m-%d_%H-%M-%S')+'.pkl')
        SaveFiles.savePokemon(backupOld, path)
        
    @staticmethod
    def syncSheetBackupSavefiles(index=0):
        '''Compares Backup at index (latest by default) with google spreadsheet and upload/downloads differences'''
        dt = datetime.now()
        backups = Backup.get(index)
        sheets = SheetCommands.downloadAllSheet()
        
        log_players = Backup.__compareGspreadBackup(SheetCommands.convertObjToRow(backups[1]), sheets[SheetName.PLAYERS], 
                                                    backups[0], Filenames.PlAYERS, SheetName.PLAYERS)
        log_wild = Backup.__compareGspreadBackup(SheetCommands.convertObjToRow(backups[2]), sheets[SheetName.WILDSPAWNS], 
                                                 backups[0], Filenames.WILD_POKEMON, SheetName.WILDSPAWNS)
        log_npcs = Backup.__compareGspreadBackup(SheetCommands.convertObjToRow(backups[3]), sheets[SheetName.NPCS], 
                                                 backups[0], Filenames.NPCS, SheetName.NPCS)
        log_leaders = Backup.__compareGspreadBackup(SheetCommands.convertObjToRow(backups[4]), sheets[SheetName.GYMLEADERS], 
                                                    backups[0], Filenames.LEADERS_GEN4, SheetName.GYMLEADERS)
        Backup.__outup_log(log_players[0], log_wild[0], log_npcs[0], log_leaders[0])
    
        for log in [log_players, log_wild, log_npcs, log_leaders]:
            if log[2] != 0:
                print("\nFound "+str(log[2])+ " differences in", log[1])
                ans = input("Press '1' to keep backup, '2' to keep sheet or '3' to do nothing.\nInput: ")
                match ans:
                    case '1': Backup.__syncSheetFromBackup(log[1:], sheets[FilenameToSheet[log[1]]], backups)
                    case '2': Backup.__syncBackupFromSheet(log[1:], sheets[FilenameToSheet[log[1]]], backups)
                    case _: pass
            else: print("\nNo differences found in", log[1])
        Backup.create()
    
    @staticmethod
    def __syncSheetFromBackup(log_info:tuple[str, int, list[list[str]]], gspread_list:list[list[str]], 
                              backups:tuple[list[datetime], list[Pokemon], list[Pokemon], list[Pokemon], list[Pokemon]]):
        '''Uploads Backup to Google Spreadsheet'''
        backup_name = log_info[0]
        ids_missing = log_info[2][0]
        ids_modified = log_info[2][1]
        ids_extra = log_info[2][2]
        temp_upload = []
        temp_remove = []
        print("Syncing sheet [", FilenameToSheet[backup_name], "]...")
        
        match backup_name:
            case Filenames.PlAYERS: backup = backups[1]
            case Filenames.WILD_POKEMON: backup = backups[2]
            case Filenames.NPCS: backup = backups[3]
            case Filenames.LEADERS_GEN4: backup = backups[4]
            case _: 
                print("Error: backup name not found. Could not sync", backup_name)
                return None
        
        for poke in backup:
            if str(poke.uniqueID) in ids_missing or str(poke.uniqueID) in ids_modified:
                temp_upload.append(poke)
        if temp_upload != []:
            print("Restoring", len(temp_upload), "missing/modified Pokemon...")
            SheetCommands.upload(temp_upload, FilenameToSheet[backup_name])
        
        for row in gspread_list:
            if row[2] in ids_extra:
                temp_remove.append(row[2])
        if temp_remove != []:
            print("Cleaning up", len(temp_remove), "extra Pokemon...")
            SheetCommands.removePokemonByID(temp_remove, FilenameToSheet[backup_name])
        
        print("Successfully synced google spreadsheets to backup!")
    
    @staticmethod
    def __syncBackupFromSheet(log_info:tuple[str, int, list[list[str]]], gpsread_list:list[list[str]], 
                              backups:tuple[list[datetime], list[Pokemon], list[Pokemon], list[Pokemon], list[Pokemon]]):
        '''Downloads current Google Spreadsheet and saves it to new backup'''
        backup_name = log_info[0]
        ids_missing = log_info[2][0]
        ids_modified = log_info[2][1]
        ids_extra = log_info[2][2]
        temp_add = []
        temp_update = []
        temp_remove = []
        print("Syncing backup [", backup_name, "]...")
        match backup_name:
            case Filenames.PlAYERS: backup = backups[1]
            case Filenames.WILD_POKEMON: backup = backups[2]
            case Filenames.NPCS: backup = backups[3]
            case Filenames.LEADERS_GEN4: backup = backups[4]
            case _: 
                print("Error: backup name not found. Could not sync", backup_name)
                return None
            
        for poke in backup:
            if str(poke.uniqueID) in ids_missing:
                temp_remove.append(poke.uniqueID)
        for row in gpsread_list:
            if row[SheetColumnCampainNum.ID] in ids_modified:
                temp_update.append(row)
            if row[SheetColumnCampainNum.ID] in ids_extra:
                temp_add.append(row)

        if temp_remove != []:
            print("Removing", len(temp_remove), "extra Pokemon from Backup...")
            PokeCommands.despawn(FilenameToPath[backup_name], temp_remove)
        
        if temp_update != []:
            print("Updating", len(temp_update), "pokemon in Backup...")
            for row in temp_update:
                PokeCommands.levelUp(FilenameToPath[backup_name], int(row[SheetColumnCampainNum.ID]), int(row[SheetColumnCampainNum.LEVEL]))
                
        if temp_add != []:
            for row in temp_add:
                moveset = [[row[SheetColumnCampainNum.MOVE1+i] for i in range(5)],
                            [row[SheetColumnCampainNum.MOVE2+i] for i in range(5)],
                            [row[SheetColumnCampainNum.MOVE3+i] for i in range(5)],
                            [row[SheetColumnCampainNum.MOVE4+i] for i in range(5)],]
                PokeCommands.spawnCustom(row[SheetColumnCampainNum.NAME], -1, -1, -1, -1, -1, -1, row[SheetColumnCampainNum.TRAINER], row[SheetColumnCampainNum.NATURE],
                                         int(row[SheetColumnCampainNum.LEVEL]), row[SheetColumnCampainNum.GENDER], row[SheetColumnCampainNum.AB], True,
                                         False, moveset, False, backup_name, row[SheetColumnCampainNum.ID])
        print("Successfully synced backup/savefiles to google spreadsheet!")
        
    @staticmethod
    def __compareGspreadBackup(backup_list: list[list[str]], gspread_list: list[list[str]], backupdate: datetime,
                               backupname:str, gspreadname:str) -> tuple[list[str], str, int, list[list[str]]]:
        '''Compares gspread with most recent backup and returns log, 
        \nbackupname, differences and ids with differences[[missing], [modified], [extra]].'''
        gspread_list.pop(0)
        dt = datetime.now()
        count_missing = 0
        count_extra = 0
        count_modified = 0
        log =["=====COMPARING: Backup [", backupname, "] from [ "+backupdate.strftime('%Y-%m-%d %H:%M:%S')+ 
              " ] with GSpreadSheet [ " + gspreadname +" ] at [ "+ dt.strftime('%Y-%m-%d %H:%M:%S')+" ]=====\n"]
        missing = []
        ids_missing = []
        extra = []
        ids_extra = []
        modified = []
        ids_modified = []
        
        sheetids = []
        backupids = []
        for row in gspread_list:
            sheetids.append(row[2])
        for row in backup_list:
            backupids.append(row[2])

        for row in gspread_list:
            if row not in backup_list:
                if row[2] not in backupids:
                    extra.append(row)
                    ids_extra.append(row[2])
                    count_extra += 1  
                
        for row in backup_list:
            if row not in gspread_list:
                if row[2] in sheetids: 
                    modified.append(row)
                    ids_modified.append(row[2])
                    count_modified += 1
                else: 
                    missing.append(row)
                    ids_missing.append(row[2])
                    count_missing += 1    
        
        log.append("Backup items missing from Spreadsheet: "+str(count_missing)+'\n')
        for row in missing:
            log.append('[')
            for i in row:
                log.append(' '+i+' |')
            log.append("]\n")
            
        log.append("\nBackup items modified from Spreadsheet: "+str(count_modified)+'\n')
        for row in modified:
            log.append('[')
            for i in row:
                log.append(' '+i+' |') 
            log.append("]\n")
                 
        log.append("\nExtra items in Spreadsheet: "+str(count_extra)+'\n')
        for row in extra:
            log.append('[')
            for i in row:
                log.append(' '+i+' |')
            log.append("]\n")
            
        differences = len(missing)+len(modified)+len(extra)
        log.append("Values checked: "+str(len(backup_list)+len(extra)))
        log.append("\nTotal differences: "+str(differences))

        return [log, backupname, differences,[ids_missing, ids_modified, ids_extra]]
    
    @staticmethod
    def __outup_log(*logs:list[str]):
        fname = "sync_log_"+datetime.now().strftime('%Y-%m-%d_%H-%M-%S')+'.txt'
        path = os.path.join(Directory.SYNC_LOGS, fname)
        with open(path, 'w') as outp:
            for log in logs:
                for line in log:
                    outp.write(line)
                outp.write('\n\n')
        print("Sync log created at: \""+ path+"\"")
        
