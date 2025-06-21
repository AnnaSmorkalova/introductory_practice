import cv2
import numpy as np

list_of_commands = {"load image":"load image for program to work with", "show image": "show loaded image", "show_blue": "show image in blue color", "show red": "show image in red color", "show green": "show image in green color", "resize": "resize image, user choose image size", "change brightness": "changes image brightness", "rectangle": "draw a blue rectangle on image" }

def load_image(img_name):
    img = cv2.imread(img_name)
    if img is not None:
        print("img successfully loaded")
        return img
    else:
        print("Error wrong img name")

def show_image(img_name):
    cv2.imshow("image", img_name)

def show_green(img_name):
    cv2.destroyAllWindows()
    cv2.imshow('Color green', img_name[:, :, 1])
    cv2.waitKey(1)

def show_blue(img_name):
    cv2.destroyAllWindows()
    cv2.imshow('Color blue', img_name[:, :, 0])
    cv2.waitKey(1)

def show_red(img_name):
    cv2.destroyAllWindows()
    cv2.imshow('Color red', img_name[:, :, 2])
    cv2.waitKey(1)

def resize(img_name, dsize):
    temp = cv2.resize(img_name, dsize)
    return temp

def change_brightness(image, brightness):
    # Применяем изменение яркости с помощью функции addWeighted
    darkened_image = np.clip(image * brightness, 0, 255).astype(np.uint8)
    return darkened_image

def rectangle(image_name, x, y, width, height):
    temp = cv2.rectangle(image_name, (x, y), (x + width, y + height), (255, 0, 0), 2)
    return temp

def main():
    while True:
        user_input = input("Input valid command or help: ")
        if user_input == "load image":
            temp = input("input image name: ")
            img = load_image(temp)
        if user_input == "show image":
            cv2.destroyAllWindows()
            cv2.imshow("Img", img)
            cv2.waitKey(1)
        if user_input == "exit":
            print("bye!")
            exit()
        if user_input == "show red:":
            show_red(img)
        if user_input == "show green":
            show_green(img)
        if user_input == "show blue":
            show_blue(img)
        if user_input == "destroy all windows":
            cv2.destroyAllWindows()
        if user_input == "resize":
            cv2.destroyAllWindows()
            try:
                width = int(input("input width of the image: "))
                height = int(input("input height of the image: "))
                dsize = (width, height)
            except ValueError:
                print("integer is required")
                continue
            img_resized = resize(img, dsize)
            cv2.imshow("img", img_resized)
            cv2.waitKey(1)
        if user_input == "change brightness":
            cv2.destroyAllWindows()
            try:
                brightness = float(input("input brightness of the image(form 0 to 1): "))
            except ValueError:
                print("integer is required")
                continue
            temp = change_brightness(img, brightness)
            cv2.imshow("img", temp)
            cv2.waitKey(1)
        if user_input == "rectangle":
            cv2.destroyAllWindows()
            try:
                x = int(input("input x coordinates: "))
                y = int(input("input y coordinates: "))
                width = int(input("input width: "))
                height = int(input("input height: "))
            except ValueError:
                print("integer is required")
                continue
            temp = rectangle(img, x, y, width, height)
            cv2.imshow("img", temp)
            cv2.waitKey(1)
        if user_input == "help":
            for k, v in list_of_commands.items():
                print(k, ':', v)

    if __name__ == "__main__":
        main()