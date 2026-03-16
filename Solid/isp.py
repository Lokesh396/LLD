"""
Interface Segregation Principle - Clients should not be forced to depend on methods they do not use.

Why does ISP Matter 

Increased cohesion, Reduced Coupling
Improved Flexibility and Reliability
Better code Readability and Maintainabiility
Enhanced Testability
Avoid Interface Pollution and LSP Violations

Common Pitfalls

1. over segregation
2. Not thinking from clients prespective
3. Lack of Cohesion
"""
from abc import ABC, abstractmethod

class MediaPlayer(ABC):
    @abstractmethod
    def play_audio(self, audio_file):
        pass

    @abstractmethod
    def stop_audio(self):
        pass

    @abstractmethod
    def adjust_audio_volume(self, volume):
        pass

    @abstractmethod
    def play_video(self, video_file):
        pass

    @abstractmethod
    def stop_video(self):
        pass

    @abstractmethod
    def adjust_video_brightness(self, brightness):
        pass

    @abstractmethod
    def display_subtitles(self, subtitle_file):
        pass

class AudioOnlyPlayer(MediaPlayer):
    def play_audio(self, audio_file):
        print(f"Playing audio file: {audio_file}")

    def stop_audio(self):
        print("Audio stopped.")

    def adjust_audio_volume(self, volume):
        print(f"Audio volume set to: {volume}")

    # Unwanted methods
    def play_video(self, video_file):
        raise NotImplementedError("Not supported.")

    def stop_video(self):
        raise NotImplementedError("Not supported.")

    def adjust_video_brightness(self, brightness):
        raise NotImplementedError("Not supported.")

    def display_subtitles(self, subtitle_file):
        raise NotImplementedError("Not supported.")
    

# Appling ISP
# Audio-only capabilities
class AudioPlayerControls(ABC):
    @abstractmethod
    def play_audio(self, audio_file):
        pass

    @abstractmethod
    def stop_audio(self):
        pass

    @abstractmethod
    def adjust_audio_volume(self, volume):
        pass

# Video-only capabilities
class VideoPlayerControls(ABC):
    @abstractmethod
    def play_video(self, video_file):
        pass

    @abstractmethod
    def stop_video(self):
        pass

    @abstractmethod
    def adjust_video_brightness(self, brightness):
        pass

    @abstractmethod
    def display_subtitles(self, subtitle_file):
        pass