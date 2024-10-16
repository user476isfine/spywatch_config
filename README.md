# Spy watch config

I made this because I was bored.

The text file format for certain spy watches contains some non-intuitive fields that one must manually edit. This is a VERY simple script and I don’t intend to support additional features.

The spy watch resets this information sometimes, but I don’t remember when and I don’t intend to look at it right now (sorry but not sorry).

Note: This project has nothing to do with any inappropriate use of spy watches that go against the law. I just searched for its configuration and automated it. Use it at your own discretion and at your own risk (which really seems to be very low IMO).

## The text fields

#### - _"Oh I would like to configure manually but I don’t know what the fields are."_ Ok.

#### - _"It would be awesome if you explain how things work."_ Ok.

The text file `settime.txt` must be at the root folder. I put an example in this repository with the format instructions. An example of a valid format is `2023-02-01 03:02:01 N 2`.

Here’s the detailed information.

### First part: date

Type the date in the format `YYYY-MM-DD`, where:

  - `YYYY` is for the year (4 digits)

  - `MM` is for the month (two digits, so include the leading 0 if needed)

  - `DD` is for the day (two digits, so include the leading 0 if needed)

### Second part: time

Type a space after the previous part and type the time in the format `HH:MM:SS`, where:

  - `HH` is for the hour in 24-hour format (two digits, so include the leading 0 if needed)

  - `MM` is for the minute (two digits, so include the leading 0 if needed)

  - `SS` is for the second (two digits, so include the leading 0 if needed) (why would anyone edit seconds btw)

### Third part: watermark option

Type a space after the previous part and type `Y` (yes) if you want the video to contain the date-time water mark nor `N` (no) otherwise.

The default setting is `Y`.

### Fourth (last) part: video resolution option

Type a space after the previous part and type `1`, `2`, or `3`, where:

  - `1` is 1080 P (1920x1080)

  - `2` is 720 P (1280x720)

  - `3` is VGA (640x480)

  

The default setting is `1`.

And that’s it.

**Note:** If you type any information that does not exist, I have no idea of what is going to happen, but my guess is that it will change everything to the default format.
Just a guess. I don’t worry whether I’m right or wrong.

If there is anything wrong with these instructions, you report an issue with the correction as if I would look at it. Other people can refer to it for further corrections if things don’t work.

Instead of making a pull request, fork this repository or whatever and advertise your new solution in a new issue for reference. If you forget to do so, good luck to those who found this repository and not yours.

I hope everything goes well, but I don’t care otherwise. Have a delightful time, though!
