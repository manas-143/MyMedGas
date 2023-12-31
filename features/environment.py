import shutil
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from playwright.sync_api import sync_playwright
import os

current_directory =os.path.abspath(os.path.join(os.getcwd(), os.pardir))


def before_all(context):
    context.p = sync_playwright().start()

    Path = f'{current_directory}\\Video'
    scrnsht=f'{current_directory}\\Screenshots'
    Path1 = f'{current_directory}\\Traces'
    is_exist = os.path.exists(Path)
    exists = os.path.exists(Path1)
    print(is_exist)
    if is_exist:
        shutil.rmtree(Path)
    Path = f'{current_directory}\\Video'
    os.mkdir(Path)
    if exists:
        shutil.rmtree(Path1)
    os.mkdir(scrnsht)
    Path1 = f'{current_directory}\\Traces'
    os.mkdir(Path1)


def before_scenario(context, scenario):
    context.browser = context.p.firefox.launch(headless=True, slow_mo=5000)
    context.tab = context.browser.new_context(
        record_video_dir="Video/",
        record_video_size={"width": 1920, "height": 1080}
    )
    context.page = context.tab.new_page()
    context.page.set_viewport_size({"width": 1920, "height": 1080})

    context.tab.tracing.start(screenshots=True, snapshots=True, sources=True)


def after_scenario(context, scenario):
    scenario_name = (scenario.name.lower().replace(' ', '_'))
    context.tab.tracing.stop(path=current_directory +f"//Traces/trace.zip")
    screenshot_path = os.path.join(current_directory, f"Screenshots/{scenario_name}.png")
    context.page.screenshot(path=screenshot_path)
    context.page.close()
    with open(screenshot_path, "rb") as screenshot_file:
        attach(
            screenshot_file.read(),
            name=f"Screenshot : {scenario_name}",
            attachment_type=AttachmentType.PNG,
        )
    context.page.video.save_as(
        f"{current_directory}/Video/{scenario.name}.webm"
    )
    context.page.video.save_as(os.path.join(current_directory, f"Video/{scenario.name}"))
    with open(
            os.path.join(current_directory, context.page.video.path()), "rb"
    ) as video_file:
        # Video
        attach(
            video_file.read(),
            name=f"Video : {scenario.name}",
            attachment_type=AttachmentType.WEBM,
        )
    attach.file(current_directory +f"//Traces/trace.zip", name="Trace viewer logs", extension=".zip")

    context.tab.close()
    context.browser.close()
