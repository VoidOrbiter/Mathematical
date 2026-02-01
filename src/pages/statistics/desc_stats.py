from PyQt5.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, 
    QGridLayout, QTextEdit, QPushButton,
    QFrame, QScrollArea
)
from PyQt5.QtCore import Qt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# ------ PAGE IMPORTS ------
from my_math.statistics.central_tendency_calculate import central_tendency_calculate
from my_math.statistics.measures_of_dispersion import sample_variance
from my_math.statistics.shape_and_relative_position import (calculate_iqr, calculate_standard_error,
                                                            calculate_skewness, calculate_excess_kurtosis)
from my_math.statistics.plots.plot_helper import create_descriptive_plot, skewness_plot

class DescStatsPage(QWidget):
    def __init__(self, main_window):
        super().__init__()

        self.root_layout = QVBoxLayout(self)
        self.root_layout.setContentsMargins(0, 0, 0, 0)
        # ------ SCROLLING ------
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setStyleSheet("QScrollArea { border: none; background-color: #1e1e1e;}")

        self.content = QWidget()
        self.content.setStyleSheet("background-color: #1e1e1e;")
        self.main_layout = QGridLayout(self.content)
        self.main_layout.setSpacing(10)
        self.main_layout.setContentsMargins(20, 20, 20, 20)

        self.main_layout.setRowStretch(11, 1)
        self.scroll.setWidget(self.content)
        self.root_layout.addWidget(self.scroll)
    

        # ------ INPUT SECTION ------
        self.x_input_label = QLabel("INPUT DATA (X):")
        self.x_input_label.setStyleSheet("font-weight: bold; color: #7f8c8d; font-size: 10px;")

        self.x_arr = QTextEdit()
        self.x_arr.setPlaceholderText("Enter numbers separated by commas or spaces...")
        self.x_arr.setStyleSheet("background-color: #1e1e1e; color: #ecf0f1; border: 1px solid #3d3d3d; border-radius: 4px;")
        self.x_arr.setFixedHeight(60)

        # Row 1 and 2
        self.main_layout.addWidget(self.x_input_label, 1, 1, 1, 4)
        self.main_layout.addWidget(self.x_arr, 2, 1, 1, 4)

        # ------ PLOT DECLARATION ------
        self.figure = Figure(figsize=(5, 3), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.figure.patch.set_facecolor('#1e1e1e')
        self.canvas.setMinimumHeight(400)

        self.figure_two = Figure(figsize=(5, 3), dpi=100)
        self.canvas_two = FigureCanvas(self.figure_two)
        self.figure_two.patch.set_facecolor('#1e1e1e')
        self.canvas_two.setMinimumHeight(400)


        ###########################
        ### CATEGORIZED WIDGETS ###
        ###########################
        
        # ------ CENTRAL TENDENCY (Row 4-5) ------
        self.arithmetic_mean = QLabel("---")
        self.geometric_mean = QLabel("---")
        self.harmonic_mean = QLabel("---")
        self.median = QLabel("---")

        central_tendency = [
            ("Arithmetic Mean", self.arithmetic_mean),
            ("Geometric Mean", self.geometric_mean),
            ("Harmonic Mean", self.harmonic_mean),
            ("Median", self.median)
        ]

        # ------ MEASURES OF DISPERSION (Row 6-7) ------
        self.sample_variance = QLabel("---")
        self.standard_deviation = QLabel("---")
        self.mean_absolute_deviation = QLabel("---")
        self.coefficient_of_variation = QLabel("---")

        measures_of_dispersion = [
            ("Sample Variance", self.sample_variance),
            ("Standard Deviation", self.standard_deviation),
            ("Mean Absolute Deviation", self.mean_absolute_deviation),
            ("Coefficient of Variation", self.coefficient_of_variation)
        ]

        # ------ SHAPE & RELATIVE POSITION (Row 8-9) ------
        self.skewness = QLabel("---")
        self.excess_kurtosis = QLabel("---")
        self.standard_error = QLabel("---")
        self.interquartile_range = QLabel("---")

        shape_and_relative_position = [
            ("Skewness", self.skewness),
            ("Excess Kurtosis", self.excess_kurtosis),
            ("Standard Error", self.standard_error),
            ("Interquartile Range", self.interquartile_range)
        ]

        # ------ POPULATING QGRIDLAYOUT ROWS ------
        self.populate_grid_row(central_tendency, row=4)
        self.populate_grid_row(measures_of_dispersion, row=6)
        self.populate_grid_row(shape_and_relative_position, row=8)

        # ------ CALCULATE BUTTON (Row 10) ------
        self.calculate_btn = QPushButton("CALCULATE")
        self.calculate_btn.setFixedHeight(40)
        self.calculate_btn.setCursor(Qt.PointingHandCursor)
        self.calculate_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                font-weight: bold;
                border-radius: 4px;
                margin-top: 10px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        self.calculate_btn.clicked.connect(self.calculate)
        
        # ------ CALCULATE BUTTON ROW 10 ------
        self.main_layout.addWidget(self.calculate_btn, 10, 1, 1, 4)

        # ------ PLOT CANVAS ROW 11-12
        self.main_layout.addWidget(self.canvas, 11, 1, 1, 4)
        self.main_layout.addWidget(self.canvas_two, 12, 1, 1, 4)

        self.canvas.hide()
        self.canvas_two.hide()

    def populate_grid_row(self, data_list, row):
        target_row = row + 1 
        for col, (title_text, widget) in enumerate(data_list):
            target_col = col + 1 
            container = QVBoxLayout()
            container.setSpacing(4)
            
            title = QLabel(title_text.upper())
            title.setStyleSheet("font-weight: bold; color: #7f8c8d; font-size: 10px; letter-spacing: 1px;")
            
            widget.setStyleSheet("""
                QLabel {
                    border: 1px solid #3d3d3d;
                    border-left: 3px solid #3498db;
                    border-radius: 4px;
                    padding: 5px;
                    background-color: #1e1e1e;
                    color: #ecf0f1;
                }
                QLabel:hover { border-color: #3498db; background-color: #252525; }
            """)
            widget.setAlignment(Qt.AlignCenter)
            widget.setFixedSize(140, 40)

            container.addWidget(title, alignment=Qt.AlignLeft)
            container.addWidget(widget)
            self.main_layout.addLayout(container, target_row, target_col)

    def calculate(self):
        raw_text = self.x_arr.toPlainText()

        if not raw_text:
            print("List is empty")
            return
        try:
            data = [float(val) for val in raw_text.replace(',', ' ').split()]
        except ValueError:
            return
           

        # ------ CENTRAL TENDENCY ------
        results = central_tendency_calculate(data)
        self.arithmetic_mean.setText(f"{results['arithmetic']:.4f}")
        
        h_val = results['harmonic']
        self.harmonic_mean.setText(f"{h_val:.4f}" if isinstance(h_val, float) else h_val)
        
        g_val = results['geometric']
        self.geometric_mean.setText(f"{g_val:.4f}" if isinstance(g_val, float) else g_val)

        median = results['median']
        self.median.setText(f"{median:.4f}" if isinstance(median, float) else median)

        # ------ MEASURES OF DISPERSION ------
        variance, std_dev, mean_absolute_deviation, coefficient_of_variation = sample_variance(data)
        self.sample_variance.setText(f"{variance:.4f}")
        self.standard_deviation.setText(f"{std_dev:.4f}")
        self.mean_absolute_deviation.setText(f"{mean_absolute_deviation:.4f}")
        self.coefficient_of_variation.setText(f"{coefficient_of_variation:.4f}")

        # ------ SHAPE & RELATIVE POSITION ------
        iqr_val     = calculate_iqr(data)
        skewness    = calculate_skewness(data)
        kurtosis    = calculate_excess_kurtosis(data)
        std_err     = calculate_standard_error(std_dev, data)
        self.interquartile_range.setText(f"{iqr_val:.4f}")
        self.skewness.setText(f"{skewness:.4f}")
        self.excess_kurtosis.setText(f"{kurtosis:.4f}")
        self.standard_error.setText(f"{std_err:.4f}")

        # ------ IQR PLOT ------
        try:
            create_descriptive_plot(self.figure, data)
            self.canvas.draw()
            self.canvas.show()
        except Exception as e:
            print(f"Plotting error: {e}")

        # ------ SKEWNESS PLOT ------
        try:
            
            skewness_plot(self.figure_two, data)

            self.figure_two.tight_layout(pad=3.0)
            self.canvas_two.draw()
            self.canvas_two.show()
        
        except Exception as e:
            print(f"plotting crash: {e}")