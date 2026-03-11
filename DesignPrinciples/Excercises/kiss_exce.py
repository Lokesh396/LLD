class DisplayNameFormatter:
    def format_display_name(self, name: str) -> str:
        # Your implementation here
        name = name.strip()
        return name.capitalize()

# Test
formatter = DisplayNameFormatter()
print(formatter.format_display_name("  john doe  "))
print(formatter.format_display_name("ALICE"))
print(formatter.format_display_name("  bob  "))




class ReportExporter:
    def export_csv(self, rows: list[list[str]]) -> str:
        # Your implementation here
        for i in range(len(rows)):
            rows[i] = ",".join(rows[i])
        return "\n".join(rows)

# Test
exporter = ReportExporter()
data = [
    ["Name", "Age", "City"],
    ["Alice", "30", "New York"],
    ["Bob", "25", "London"]
]
print(exporter.export_csv(data))