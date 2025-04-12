import gifos

t = gifos.Terminal(width=320, height=240, xpad=5, ypad=5)
t.gen_text(text="Hello World!", row_num=1)
t.gen_text(text="Hello VizXtreme and ukriu!", row_num=2)
github_stats = gifos.utils.fetch_github_stats(
    user_name="rickastleey"
)  # needs GITHUB_TOKEN in .env or as environment variable
t.delete_row(row_num=1)
t.gen_text(text=f"GitHub Name: {github_stats.user_name}", row_num=1, contin=True)
t.gen_gif()
image = gifos.utils.upload_imgbb(
    file_name="output.gif", expiration=60
)  # needs IMGBB_API_KEY in .env or as environment variable
print(image.url)