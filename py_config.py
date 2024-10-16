import datetime
import sys

SENTENCES = {}
SENTENCES["DATE_CHOICE_INSTRUCTIONS"] = "\nDefine the intended recording date, by:\n- typing the date in \"YYYY-MM-DD\" format,\n- typing \"tomorrow\" for tomorrow's date, or\n- pressing Enter for the current date.\n\n-> "
SENTENCES["TIME_CHOICE_INSTRUCTIONS"] = "\nSet the time (type the time in \"HH:MM\" format, 24-hour), or press Enter for the current time.\n\n-> "
SENTENCES["INVALID_DATE_TIME_CHOICE"] = "\nCould not identify a valid date and time format. Setting to current date and time by default."

SENTENCES["WATERMARK_CHOICE_INSTRUCTIONS"] = "\nShould the recording contain a date watermark? (Y/N)\n\n-> "
SENTENCES["INVALID_WATERMARK_CHOICE"] = "\nThe displaying of date watermark is neither set to \"Yes\" (\"Y\") nor \"No\" (\"N\").\nSetting to \"Y\" by default."

SENTENCES["VIDEO_RESOLUTION_CHOICE_INSTRUCTIONS"] = "\nChoose a video resolution option:\n  1: 1080 P (1920x1080)\n  2: 720 P (1280x720)\n  3: VGA (640x480)\n-> "
SENTENCES["INVALID_VIDEO_RESOLUTION_CHOICE"] = "\nThe video resolution option is not valid; it should be \"1\" (1080 P, 1920x1080), \"2\" (720 P, 1280x720), or \"3\" (VGA, 640x480).\nSetting to \"1\" by default."


'''Expected string content format: 2021-01-01 00:00:00 Y 1 ([date] [time] [watermark] [resolution])'''
def set_config(date_and_time, should_display_date_watermark, video_resolution_option = "1"):
  date_file = open("settime.txt", "w")

  if (not(date_and_time)):
    print(SENTENCES["INVALID_DATE_TIME_CHOICE"])
    # Obtain the current date and time in the format YYYY-MM-DD HH:MM:SS
    date_and_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

  # "Y" for diplaying date and time watermark in the recording, "N" otherwise
  if (should_display_date_watermark != "Y" and should_display_date_watermark != "N"):
    print(SENTENCES["INVALID_WATERMARK_CHOICE"])
    should_display_date_watermark = "Y"

  # Video resolution options: "1" - 1080 P (1920x1080), "2": 720 P (1280x720), "3": VGA (640x480)
  if (int(video_resolution_option) < 1 or int(video_resolution_option) > 3):
    print(SENTENCES["INVALID_VIDEO_RESOLUTION_CHOICE"])
    video_resolution_option = "1"

  final_content = date_and_time + " " + should_display_date_watermark.upper() + " " + video_resolution_option
  date_file.write(final_content)
  date_file.close()

def main():
  date_time_option = "NOT_CHOSEN_YET"
  invalid_option = True

  date = datetime.datetime.today()
  while (invalid_option):
    date_time_option = str(input(SENTENCES["DATE_CHOICE_INSTRUCTIONS"])).strip()
    if (date_time_option != ""):
      if (date_time_option == "tomorrow"):
        date = datetime.datetime.now() + datetime.timedelta(days = 1)
      else:
        try:
          date = datetime.datetime.strptime(date_time_option, "%Y-%m-%d")
        except:
          continue
    invalid_option = False
  date = date.strftime("%Y-%m-%d")

  date_time_option = "NOT_CHOSEN_YET"
  invalid_option = True

  time = datetime.datetime.now()
  while (invalid_option):
    date_time_option = str(input(SENTENCES["TIME_CHOICE_INSTRUCTIONS"])).strip()
    if (date_time_option != ""):
      try:
        time = datetime.datetime.strptime(date_time_option, "%H:%M")
      except:
        continue
    invalid_option = False
  time = time.strftime("%H:%M:%S")

  should_display_date_watermark = str(sys.argv[1]).upper() if (len(sys.argv[1:]) > 0) else "?"
  while (not(should_display_date_watermark in ["Y", "N"])):
    should_display_date_watermark = str(input(SENTENCES["WATERMARK_CHOICE_INSTRUCTIONS"])).strip().upper()

  video_resolution_option = str(sys.argv[2]) if (len(sys.argv[1:]) > 1) else "0"
  while (not(video_resolution_option in ["1", "2", "3"])):
    video_resolution_option = str(input(SENTENCES["VIDEO_RESOLUTION_CHOICE_INSTRUCTIONS"])).strip()

  set_config(date + " " + time, should_display_date_watermark, video_resolution_option)
  print("\nDone! Wow, that was fast, huh?")

if __name__ == "__main__":
  sys.exit(main())
