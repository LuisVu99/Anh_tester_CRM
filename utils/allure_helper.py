import allure
from pathlib import Path
from playwright.sync_api import sync_playwright, Browser, BrowserContext


class AllureHelper:
    @staticmethod
    def attach_log(file_path: Path):
        
        if file_path.exists():
            allure.attach.file(
                str(file_path),
                name = "automation log",
                attachment_type=allure.attachment_type.TEXT
        )

    @staticmethod
    def attach_screenshot(screenshot_path: Path):
        
        allure.attach.file(
            str(screenshot_path),
            name = "Failure Screenshot",
            attachment_type=allure.attachment_type.PNG
        )

    @staticmethod
    def attach_video(video_path: Path):
        
        allure.attach.file(
            str(video_path),
            name = "Failure video",
            attachment_type=allure.attachment_type.WEBM
        )

    # @staticmethod
    # def attach_trace(trace_path: Path):
    #     allure.attach.file(
    #         str(trace_path),
    #         name = "Failure trace",
    #         attachment_type=allure.attachment_type.ZIP
    #     )

    @staticmethod
    def start_trace(context: BrowserContext):
        """
        Start Playwright Trace
        """
        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )

    @staticmethod
    def stop_trace(context: BrowserContext, trace_path: Path):
        """
        Stop trace and save trace.zip
        """
        trace_path.parent.mkdir(parents=True, exist_ok=True)

        context.tracing.stop(
            path=str(trace_path)
        )

    @staticmethod
    def attach_trace(trace_path: Path):
        """
        Attach trace.zip to Allure
        """
        if trace_path.exists():
            allure.attach.file(
                str(trace_path),
                name="Playwright Trace",
                attachment_type=allure.attachment_type.ZIP
            )

