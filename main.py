import gifos

# Initialize the Terminal object
t = gifos.Terminal(
    width=800,
    height=600,
    xpad=5,
    ypad=5,
    font_size=15,
)

# Set the frames per second
t.set_fps(15)

t.gen_text("C:\\Users\\xnggypr\\Downloads\\platform-tools>", 1)
t.gen_typing_text(text="adb devices", row_num=1, col_num=10, contin=True, speed=0.3)
t.gen_text("* daemon is not running; starting now at tcp:5037", 2)
t.gen_text("* daemon started successfully", 3)
t.gen_text("List of devices attached", 4)
t.gen_text("2312DRAABG device", 5)
t.gen_text("C:\\Users\\xnggypr\\Downloads\\platform-tools>", 7)
t.gen_typing_text(text="adb reboot bootloader", row_num=7, col_num=10, contin=True, speed=0.3)
t.gen_text("C:\\Users\\xnggypr\\Downloads\\platform-tools>", 9)
t.gen_typing_text(text="fastboot devices", row_num=9, col_num=10, contin=True, speed=0.3)
t.gen_text("2312DRAABG                fastboot", 10)
t.gen_text("C:\\Users\\xnggypr\\Downloads\\platform-tools>", 12)
t.gen_typing_text(text='echo "Dont do this with your device!"', row_num=12, col_num=10, contin=True, speed=0.3)
t.gen_text("Dont do this with your device!", 13)
t.gen_text("C:\\Users\\xnggypr\\Downloads\\platform-tools>", 14)
t.gen_typing_text(text="fastboot erase lk", row_num=14, col_num=10, contin=True, speed=0.3)
t.gen_text("erasing 'lk'...", 15)
t.gen_text("OKAY [0.036s]", 16)
t.gen_text("finished. total time: 0.037s", 17)
t.gen_text("C:\\Users\\xnggypr\\Downloads\\platform-tools>", 19)
t.gen_typing_text(text="fastboot reboot", row_num=19, col_num=10, contin=True, speed=0.3)
t.gen_text("rebooting...", 20)
t.gen_text("finished. total time: 0.000s", 22)
t.gen_text("C:\\Users\\xnggypr\\Downloads\\platform-tools>", 24)
t.gen_typing_text(text='echo "Oh... My device is not booting anymore! What to do?"', row_num=24, col_num=10, contin=True, speed=0.3)
t.gen_text("Oh... My device is not booting anymore! What to do?", 25)
t.gen_text("C:\\Users\\xnggypr\\Downloads\\platform-tools>", 26)
# Generate the GIF
t.gen_gif()
