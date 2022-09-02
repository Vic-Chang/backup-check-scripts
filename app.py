import os
import argparse
import dictdiffer


def create_dummy_data():
    """
    Create dummy data for test
    """
    dummy_root_folder = 'Dummy_data'
    os.mkdir(dummy_root_folder)
    for index, folder in enumerate(range(5)):
        folder = os.path.join(dummy_root_folder, str(index + 1))
        os.mkdir(folder)
        for item_index, item in enumerate(range(10)):
            with open(os.path.join(folder, str(item_index + 1) + '.txt'), 'w+') as f:
                f.write('Dummy_data' * 2 ** 10)


def process(source_folder: str, target_folder: str) -> None:
    # Get all files and it owns size
    replace_sign = '@@@'

    def get_all_files_dict(folder_path) -> dict:
        files_info_dict = {}
        for root, directories, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_size = os.stat(file_path).st_size
                files_info_dict[file_path.replace(folder_path, replace_sign)] = file_size
        return files_info_dict

    source_files_info_dict = get_all_files_dict(source_folder)
    target_files_info_dict = get_all_files_dict(target_folder)

    change_list = []
    un_backup_list = []
    for diff in list(dictdiffer.diff(source_files_info_dict, target_files_info_dict)):
        if diff[0] == 'change':
            change_list.append((diff[1], diff[2]))
        elif diff[0] == 'remove':
            un_backup_list = diff[2]

    # Write to file
    with open('backup_change_list.txt', 'w', encoding='cp950') as f:
        for item in change_list:
            try:
                f.write(item[0][0].replace(replace_sign, target_folder) + '\n')
            except:
                f.write('--------------' + '\n')

    with open('Un_Backup_List.txt', 'w', encoding='cp950') as f:
        for item in un_backup_list:
            try:
                f.write(item[0].replace(replace_sign, target_folder) + '\n')
            except:
                f.write('--------------' + '\n')


if __name__ == '__main__':
    # create_dummy_data()

    parser = argparse.ArgumentParser()
    parser.add_argument('source', type=str, help='Source folder')
    parser.add_argument('target', type=str, help='Target folder')
    args = parser.parse_args()

    print(f'Source folder: {args.source}')
    print(f'Backup folder: {args.target}')
    print('Processing, please wait ...')
    process(args.source, args.target)
    print('Success ! Results has been written to text files!')
