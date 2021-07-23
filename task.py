from variables import *


def save_file_into_work_item(local_filepath, replace=False):
    new_workitem_filename = workitem_filename
    if replace:
        items.remove_work_item_file(workitem_filename)
        items.save_work_item()
    else:
        new_workitem_filename = f"updated_{workitem_filename}"
    items.add_work_item_file(local_filepath, new_workitem_filename)
    items.save_work_item()


def add_new_data_row_to_csv_file(filepath, row):
    data = tables.read_table_from_csv(filepath)
    tables.add_table_row(data, row)
    tables.write_table_to_csv(data, filepath)


def minimal_task():
    items.load_work_item_from_environment()
    local_data_filepath = items.get_work_item_file(workitem_filename)
    with open(local_data_filepath, "r") as fin:
        print(fin.read())
    add_new_data_row_to_csv_file(local_data_filepath, [4, "ship"])
    # create new workitem file with "updated_" prefix
    save_file_into_work_item(local_data_filepath)
    # remove old workitem file and recreate it with new content
    save_file_into_work_item(local_data_filepath, True)
    print("Done.")


if __name__ == "__main__":
    minimal_task()
