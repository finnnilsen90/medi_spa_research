import re
from MediForecastAssumptions import MediForecastAssumptions

# Read existing README
with open("README.md", "r") as f:
    content = f.read()

# Build services list
service_list = "\n".join(f"- {i[0]}" for i in MediForecastAssumptions().services.items())
new_section_services = f"### Services\n{service_list}"

# Build initial investment list
new_initial_investment = f"${sum(MediForecastAssumptions().initial_investment.values()):,}"
# Build monthly fixed cost list
new_monthly_fixed_costs = f"${sum(MediForecastAssumptions().fixed_opex.values()):,}"

# Replace section between markers
updated_services = re.sub(
    r"<!-- SERVICES START -->.*<!-- SERVICES END -->",
    f"<!-- SERVICES START -->\n{new_section_services}\n<!-- SERVICES END -->",
    content,
    flags=re.DOTALL
)

updated_monthly_fixed_costs = re.sub(
    r"<!-- MONTHLY_FIXED_COSTS START -->.*<!-- MONTHLY_FIXED_COSTS END -->",
    f"<!-- MONTHLY_FIXED_COSTS START -->\n{new_monthly_fixed_costs}\n<!-- MONTHLY_FIXED_COSTS END -->",
        content,
    flags=re.DOTALL
)

final_update = re.sub(
    r"<!-- INITIAL_INVESTMENT START -->.*<!-- INITIAL_INVESTMENT END -->",
    f"<!-- INITIAL_INVESTMENT START -->\n{new_initial_investment}\n<!-- INITIAL_INVESTMENT END -->",
    updated_monthly_fixed_costs,
    flags=re.DOTALL
)

with open("README.md","w") as f:
    f.write(final_update)