import csv
from police_api import PoliceAPI
from police_api.forces import Force


def main():
    filename = "police.csv"

    api = PoliceAPI()

    forces = api.get_forces()

    field_names = ["name", "url"]
    with open(filename, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names, delimiter=";")
        writer.writeheader()
    for i in forces:
        tu = Force(api, id=i.id)
        police_data = tu.engagement_methods
        force_1 = str(tu)
        force = force_1.replace("<Force>", "")
        for k in police_data:
            p = k["url"], k["title"]
            if p[0] != "" and p[1] == "facebook":
                response = dict({"name": force, "url": p[0]})
                with open(filename, "a", newline="") as csvfile:
                    writer = csv.DictWriter(
                        csvfile, fieldnames=field_names, delimiter=";"
                    )
                    writer.writerow(response)
                    print(response)


if __name__ == "__main__":
    main()
