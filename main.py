import streamlit as st
from pytube import YouTube

# get the title
# yt.title
link = ""

# get the
# yt.thumbnail_url
st.title('fataudio');
def main():
    st.title("YouTube MP3 Downloader")

    # Input field for the YouTube URL
    video_url = st.text_input("Enter YouTube URL")

    # Select output directory
    download_path = st.text_input("Enter output directory path", "/Users/fat/Downloads/GuncelListe")

    if st.button("Download MP3"):
        if video_url:
            try:
                youtube = YouTube(video_url)
                audio_stream = youtube.streams.filter(only_audio=True).first()
                audio_stream.download(output_path=download_path, filename=f"{youtube.title}.mp3")
                st.success("Download completed!")
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a valid YouTube URL.")

if __name__ == "__main__":
    main()

