from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    silver_service_taxi = SilverServiceTaxi("Hummer", 100, 2)
    silver_service_taxi.drive(18)
    print(silver_service_taxi)
    print(silver_service_taxi.get_fare())


main()
