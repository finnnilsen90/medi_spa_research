# Read existing README
with open("README.md", "r") as f:
    content = f.read()

# Build services list
service_list = "\n".join(f"- {i[0]}" for i in services)
new_section = f"## Services\n{service_list}"

# Replace section between markers
import re
updated = re.sub(
    r"<!-- SERVICES START -->.*<!-- SERVICES END -->",
    f"<!-- SERVICES START -->\n{new_section}\n<!-- SERVICES END -->",
    content,
    flags=re.DOTALL
)

with open("README.md", "w") as f:
    f.write(updated)