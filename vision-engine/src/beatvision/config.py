from dataclasses import dataclass


@dataclass(slots=True)
class CameraConfig:
    index: int = 0
    width: int = 1280
    height: int = 720
    fps: int = 60


@dataclass(slots=True)
class WindowConfig:
    title: str = "BeatVision"
    show_fps: bool = True


@dataclass(slots=True)
class AppConfig:
    camera = CameraConfig()
    window = WindowConfig()