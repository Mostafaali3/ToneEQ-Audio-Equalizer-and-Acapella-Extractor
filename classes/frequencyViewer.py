from classes.CustomSignal import CustomSignal
import pyqtgraph as pg
import numpy as np

class FrequencyViewer(pg.PlotWidget):
    def __init__(self , current_signal:CustomSignal = None, scale = 'linear'):
        super().__init__()
        self.current_signal = current_signal
        self.showGrid(x= True, y= True , alpha = 0.25)
        self.view_scale = scale

    def plot_freq_domain(self):
        self.clear()
        signal_rfft_result_magnitudes = np.abs(self.current_signal.new_linear_frequency[1])
        if(self.view_scale == "Linear"):
            self.setLogMode(x=False, y=False)
            self.plot(self.current_signal.new_linear_frequency[0] , list(signal_rfft_result_magnitudes), pen=pg.mkPen(color = 'b' , width=1))
            # self.setYRange(min(self.current_signal.new_linear_frequency[1]),max(self.current_signal.new_linear_frequency[1]))
        
        elif(self.view_scale == "Audiogram"):
            self.setLogMode(x=True, y=False)
            self.plot(self.current_signal.new_linear_frequency[0] , signal_rfft_result_magnitudes, pen=pg.mkPen(color = 'b' , width=1))
            # self.setYRange(min(self.current_signal.new_linear_frequency[1]),max(self.current_signal.new_linear_frequency[1]))
            
            
    @property
    def current_signal(self):
        return self.__current_signal
    
    @current_signal.setter
    def current_signal(self, new_signal):
        self.__current_signal = new_signal
    