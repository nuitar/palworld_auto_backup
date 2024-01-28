import os
import time
import sys

# for i in range(1, len(sys.argv)):
#     print(sys.argv[i])


def AutoBackup(archive_num: str, destination: str):
    """自动备份

    Args:
        archive_num (_type_): 存档编号
        destination (_type_): 保存备份的路径
    """
    # 删除前五个
    archives = os.listdir(destination)
    archives_count = len(archives)
    print(f'the archive\'s length is {archives_count}')
    
    if archives_count > 4:
        archives.sort()
        for file in archives[:archives_count-4]:
            os.remove(f'{destination}/{file}')
            print(f'remove {file}')
    # 备份
    base_path = '/home/steam/Steam/steamapps/common/PalServer/Pal/Saved/SaveGames/0/'
    os.system(
        f'(cd {base_path} && zip -r {destination}/$(date +%Y%m%d-%H%M).zip {archive_num}/)')
    print('success!')


if __name__ == '__main__':
    AutoBackup('749BE6ACB97148F69D8BFAC53894C3C7', '/root/pal_backup')
