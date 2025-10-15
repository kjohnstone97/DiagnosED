import ecds_V1
from shiny import App, ui, render, reactive
from datetime import datetime


app_ui = ui.page_fluid(
    ui.h2("ECDS Diagnosis Finder"),
    ui.h3("This app recommends valid diagnoses from the Emergency Care Data Set, it does not replace clinical judgement."
          "\n The user holds all responsibility to ensure the accuracy of clinical documentation"
          "\n Please do not enter any patient identifiable information"),
    ui.panel_well(
        ui.input_text("input_text",
                      "Write your impression, and we will recommend valid entries:",
                      placeholder="Your impression"),
        ui.input_action_button("go_button", "Find Diagnosis"),
        ui.output_ui("result"),
    )
)

t = datetime.now().isoformat()

def server(input, output, session):
    @render.ui
    @reactive.event(input.go_button)
    def result():
        diagnosis_list = []
        impression = input.input_text()
        diagnoses = ecds_V1.top_matches(impression, n=10)
        for d in diagnoses:
            diagnosis_list.append("%s %s %s match" % (d[0], int(d[1] * 100), "%"))
        html = "<pre>" + "\n".join(diagnosis_list) + "</pre>"
        t = datetime.now().isoformat()
        return ui.HTML(html)

app = App(app_ui, server)