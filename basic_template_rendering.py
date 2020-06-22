import jinja2
import os


def generate_inventory(hostfile="hosts.txt", vendor="arista", group=""):
    loader = jinja2.FileSystemLoader(os.getcwd())
    jenv = jinja2.Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)
    template = jenv.get_template('inventory_template.j2')

    with open(hostfile, "r") as host_file:
        hosts = host_file.read().split("\n")
        print(template.render(hosts=hosts, vendor=vendor, group=group))


def main():
    generate_inventory(group="core_switch")

    
if __name__ == '__main__':
    main()
