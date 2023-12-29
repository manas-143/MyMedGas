import shutil

# from allure_commons._allure import attach
# from allure_commons.types import AttachmentType
from playwright.sync_api import sync_playwright
import os

current_directory = os.getcwd()


def before_all(context):
    context.p = sync_playwright().start()

    # Path = f'{current_directory}\Video'
    # Path1 = f'{current_directory}\Traces'
    #
    # is_exist = os.path.exists(Path)
    # is_exist1 = os.path.exists(Path1)
    # print(is_exist)
    # print(is_exist1)
    # if is_exist and is_exist1:
    #     shutil.rmtree(Path)
    #     shutil.rmtree(Path1)
    # Path = f'{current_directory}\Video'
    # Path1 = f'{current_directory}\Traces'
    # os.mkdir(Path)
    # os.mkdir(Path1)

def before_scenario(context, scenario):
    context.browser = context.p.chromium.launch(headless=False, slow_mo=5000)
    context.tab = context.browser.new_context(
        record_video_dir="Video/",
        record_video_size={"width": 1500, "height": 1200}
    )
    context.page = context.tab.new_page()
    # context.tab.tracing.start(screenshots=True, snapshots=True, sources=True)


def after_scenario(context, scenario):
    scenario_name = (scenario.name.lower().replace(' ', '_'))
    # context.tab.tracing.stop(path=current_directory +f"\\Traces\\{scenario_name}trace.zip")
    context.page.close()
    # context.page.video.save_as(
    #     f"{current_directory}/Video/{scenario.name}.webm"
    # )
    # context.page.video.save_as(os.path.join(current_directory, f"Video/{scenario.name}"))
    # with open(
    #         os.path.join(current_directory, context.page.video.path()), "rb"
    # ) as video_file:
    #     # Video
    #     attach(
    #         video_file.read(),
    #         name=f"Video : {scenario.name}",
    #         attachment_type=AttachmentType.WEBM,
    #     )
    # attach.file(current_directory +"\\Traces", name="Trace viewer logs", extension=".zip")
