from customSignal import CustomSignal
import pyqtgraph as pg
import numpy as np

class FrequencyViewer(pg.PlotWidget):
    def __init__(self , current_signal:CustomSignal = None , scale = 'Linear'):
        super().__init__()
        self.current_signal = current_signal
        self.showGrid(x= True, y= True , alpha = 0.25)
        self.view_scale = scale

    def plot_freq_domain(self):
        self.clear()
        signal_rfft_result_magnitudes = np.abs(self.current_signal.new_linear_frequency[1])
        if(self.view_scale == "Linear"):
            self.plot(self.current_signal.new_linear_frequency[0] , signal_rfft_result_magnitudes, pen=pg.mkPen(color = 'b' , width=1))
            # self.setYRange(min(self.current_signal.new_linear_frequency[1]),max(self.current_signal.new_linear_frequency[1]))
        
        elif(self.view_scale == "Audiogram"):
            self.plot(self.current_signal.new_linear_frequency[0] , signal_rfft_result_magnitudes, pen=pg.mkPen(color = 'b' , width=1))
            # self.setYRange(min(self.current_signal.new_linear_frequency[1]),max(self.current_signal.new_linear_frequency[1]))