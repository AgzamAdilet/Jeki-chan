from abc import ABC, abstractmethod
class ReportGenerator(ABC):
    def generate_report(self):
        self.collect_data()
        self.format_header()
        self.format_body()
        if self.customer_wants_save():
            self.save_report()

    def collect_data(self): print("Деректер жиналды...") [cite: 175]
    
    @abstractmethod
    def format_header(self): pass
    @abstractmethod
    def format_body(self): pass

    def save_report(self): print("Есеп файлға сақталды.") [cite: 169]

    def customer_wants_save(self): 
        return input("Сақтау керек пе? (y/n): ").lower() == 'y'


class PdfReport(ReportGenerator):
    def format_header(self): print("PDF тақырыбы жасалды")
    def format_body(self): print("PDF мазмұны толтырылды")

class ExcelReport(ReportGenerator):
    def format_header(self): print("Excel кесте басы жасалды")
    def format_body(self): print("Excel ұяшықтары толтырылды")
