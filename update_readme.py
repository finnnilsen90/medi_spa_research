from MediSpaAssumptions import MediAssumptions

services = MediAssumptions().services
initial_investment = sum(MediAssumptions().initial_investment.values())



# Read existing README
with open("README.md", "r") as f:
    content = f.read()

# Build services list
service_list = "\n".join(f"- {i[0]}" for i in services.items())
new_section_services = f"### Services\n{service_list}"

# Build initial investment list
new_initial_investment = f"{initial_investment}"

# Replace section between markers
import re
updated_services = re.sub(
    r"<!-- SERVICES START -->.*<!-- SERVICES END -->",
    f"<!-- SERVICES START -->\n{new_section_services}\n<!-- SERVICES END -->",
    content,
    flags=re.DOTALL
)

updated_initial_investment = re.sub(
    r"<!-- INITIAL_INVESTMENT START -->.*<!-- INITIAL_INVESTMENT END -->",
    f"<!-- INITIAL_INVESTMENT START -->\n{new_initial_investment}\n<!-- INITIAL_INVESTMENT END -->",
    content,
    flags=re.DOTALL
)

with open("README.md","w") as f:
    f.write(updated_services)
    f.write(updated_initial_investment)