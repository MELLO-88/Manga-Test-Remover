from engine.sort_file_names import sort_file_names
from engine.join_file_path import join_file_path
from engine.get_folder_name import get_folder_name
from engine.create_folder_in_directory import create_folder_in_directory
from engine.detect_text import detect_text
from engine.get_image import get_image_height,get_image_width
from engine.find_paragraph import find_paragraph
from engine.draw_rectangles import draw_rectangles
from engine.list_folders import list_folders
from engine.open_and_return_folder import open_and_return_folder

print("Select Manga Folder")
folder_path = open_and_return_folder()
print("Select Save Folder")
output_path = open_and_return_folder()

# folder_path = 'C:/Users/kaung/Downloads/Telegram Desktop/Tokyo Ghoul/Tokyo Ghoul'
# output_path = "C:/Users/kaung/OneDrive/Desktop/Manga/Testing data/Result/Tokyo Ghoul"

def main(folder_path,output_path):
    files = sort_file_names(folder_path)

    output_folder_name = get_folder_name(folder_path)

    new_folder_path =  create_folder_in_directory(output_path,output_folder_name)

    for file in files:

        file_name = join_file_path(folder_path,file)

        print(file_name)

        text_location = detect_text(file_name)

        x_diff = get_image_width(file_name)

        y_diff = get_image_height(file_name)

        paragraph = find_paragraph(text_location,x_diff,y_diff)

        print(paragraph)

        draw_rectangles(file_name,paragraph,new_folder_path,file)





if __name__ == '__main__':
    # folder_list = list_folders(folder_path)
    # for i in folder_list:
    #     location = join_file_path(folder_path,i)
    #     print(location)
    main(folder_path, output_path)