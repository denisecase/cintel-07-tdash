import seaborn as sns
from faicons import icon_svg

from shiny import reactive
from shiny.express import input, render, ui
import palmerpenguins 

# Load the Data
df = palmerpenguins.load_penguins()

# Define the Shiny UI Page layout
ui.page_opts(title="P7 Test Penguins", fillable=True)

# Add a Shiny UI sidebar for user interaction
with ui.sidebar(title="Filter Controls"):
    ui.input_slider("mass", "Mass", 2000, 6000, 6000)

    # Use ui.input_checkbox_group() to create a checkbox group input
    ui.input_checkbox_group(
        "species",
        "Species",
        ["Adelie", "Gentoo", "Chinstrap"],
        selected=["Adelie", "Gentoo", "Chinstrap"],
    )
    ui.hr()
    ui.h6("Links")
    ui.a(
        "GitHub Source",
        href="https://tesfamariam100.github.io/cintel-07-tdash/",
        target="_blank",
    )
    ui.a(
        "GitHub App",
        href="https://tesfamariam100.github.io/cintel-07-tdash/",
        target="_blank",
    )

    # Use ui.a() to add a hyperlinks to the sidebar
    ui.a(
        "GitHub Issues",
        href="https://tesfamariam100.github.io/cintel-07-tdash/issues",
        target="_blank",
    )
    ui.a("PyShiny", href="https://shiny.posit.co/py/", target="_blank")
    ui.a(
        "Template: Basic Dashboard",
        href="https://shiny.posit.co/py/templates/dashboard/",
        target="_blank",
    )
    ui.a(
        "See also",
        href="https://github.com/denisecase/pyshiny-penguins-dashboard-express",
        target="_blank",
    )

# Use ui.layout_column_wrap to create value boxes
with ui.layout_column_wrap(fill=False):
    # Call ui.value_box to create a value box within the ui.layout_column_wrap()
    with ui.value_box(showcase=icon_svg("earlybirds")):
        "Total Number of Penguins"
        
        @render.text
        def count():
            return filtered_df().shape[0]

    # Call ui.value_box to create a value box within the ui.layout_column_wrap()
    with ui.value_box(showcase=icon_svg("ruler-horizontal")):
        "Average Bill Length"

        @render.text
        def bill_length():
            return f"{filtered_df()['bill_length_mm'].mean():.1f} mm"

    # Call ui.value_box to create a value box within the ui.layout_column_wrap()
    with ui.value_box(showcase=icon_svg("ruler-vertical")):
        "Average Bill Depth"

        @render.text
        def bill_depth():
            return f"{filtered_df()['bill_depth_mm'].mean():.1f} mm"

# Use ui.layout_columns() to create a two-column layout
with ui.layout_columns():
    with ui.card(full_screen=True):
        ui.card_header("Bill Length and Depth")

        @render.plot
        def length_depth():
            return sns.scatterplot(
                data=filtered_df(),
                x="bill_length_mm",
                y="bill_depth_mm",
                hue="species",
            )
 # Create card within columns using ui.card()
    with ui.card(full_screen=True):
        ui.card_header("Penguin Data")

 # Create a data grid using dataframe from library.
        @render.data_frame
        def summary_statistics():
            cols = [
                "species",
                "island",
                "bill_length_mm",
                "bill_depth_mm",
                "body_mass_g",
            ]
            return render.DataGrid(filtered_df()[cols], filters=True)

#ui.include_css(app_dir / "styles.css")
@reactive.calc
def filtered_df():
    filt_df = df[df["species"].isin(input.species())]
    filt_df = filt_df.loc[filt_df["body_mass_g"] < input.mass()]
    return filt_df

