from variables import *
from pathlib import Path
import shutil


def save_file_into_work_item(local_filepath, as_child=False):
    if as_child:
        current_item = items.get_current_work_item()
        items.create_output_work_item(files=[local_filepath], save=True)
        items.set_current_work_item(current_item)
    else:
        new_workitem_filename = f"updated_{workitem_filename}"
        new_file = shutil.copy(local_filepath, Path(local_filepath).with_name(new_workitem_filename))
        items.add_work_item_file(new_file, name=new_workitem_filename)
        items.save_work_item()
        print_file_contents(items.get_work_item_file(workitem_filename, TEMP_DIR / 'temp.csv'))
        print_file_contents(items.get_work_item_file(new_workitem_filename))


def add_new_data_row_to_csv_file(filepath, row):
    data = tables.read_table_from_csv(filepath)
    tables.add_table_row(data, row)
    tables.write_table_to_csv(data, filepath)


def print_file_contents(filepath):
    with open(filepath, "r") as fin:
        print(f"Contents of {filepath}:")
        print(fin.read())

def minimal_task():
    items.get_input_work_item()
    TEMP_DIR.mkdir(exist_ok=True)
    local_data_filepath = items.get_work_item_file(workitem_filename, TEMP_DIR / 'data.csv')
    print_file_contents(local_data_filepath)
    add_new_data_row_to_csv_file(local_data_filepath, [4, "ship"])
    print_file_contents(local_data_filepath)
    # create new workitem file with "updated_" prefix
    save_file_into_work_item(local_data_filepath)
    # save workitem to a child work item.
    save_file_into_work_item(local_data_filepath, as_child=True)
    print("Done.")


if __name__ == "__main__":
    minimal_task()
