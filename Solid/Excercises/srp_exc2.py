# Before: One class doing three unrelated jobs
class ReportManager:
    def create_and_send_report(self, recipient: str):
        # Responsibility 1: Generate report data
        data = [
            ["Name", "Sales", "Region"],
            ["Alice", "15000", "North"],
            ["Bob", "22000", "South"],
            ["Charlie", "18000", "East"],
        ]

        # Responsibility 2: Format as CSV
        csv_lines = []
        for row in data:
            csv_lines.append(",".join(row))
        csv_output = "\n".join(csv_lines)

        # Responsibility 3: Distribute via email
        print(f"Sending report to: {recipient}")
        print(csv_output)
        print("Report sent successfully.")

# TODO: Refactor into ReportGenerator, ReportFormatter, and ReportDistributor.

class ReportGenerator:

    def generate(self):
        print('Generating Report')
        return [
            ["Name", "Sales", "Region"],
            ["Alice", "15000", "North"],
            ["Bob", "22000", "South"],
            ["Charlie", "18000", "East"],
        ]

class ReportFormatter:

    def format_as_csv(self,data):
        print('Data is formatting to csv')
        csv_lines = []
        for row in data:
            csv_lines.append(",".join(row))
        csv_output = "\n".join(csv_lines)
        return csv_output
    def format_as_json(self,data):
        print('Data is formatting to json')
        return data
    
class ReportDistributor:

    def distribute(self, email, data):
        print(f'sending report to {email}')
        print(data)
        print('Report sent Succesfully!')
if __name__ == "__main__":
    # After refactoring, usage should look like:
    generator = ReportGenerator()
    formatter = ReportFormatter()
    distributor = ReportDistributor()
    data = generator.generate()
    formatted = formatter.format_as_csv(data)
    distributor.distribute("manager@company.com", formatted)