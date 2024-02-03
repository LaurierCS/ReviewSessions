#include <stdio.h>

// Typedef for the car struct
typedef struct Car {
    char name[50];  
    int year;
} CAR;

// Typedef for the tow truck struct
typedef struct TowTruck {
    char name[50];      
    CAR *towedCar;      // Pointer to the car being towed
} TOWTRUCK;

// Function to simulate towing
void towCar(TOWTRUCK *towTruck, CAR *car) {
    towTruck->towedCar = car;
}

int main() {
    // Create a car (Lightning McQueen)
    CAR lightningMcQueen = {"Lightning McQueen", 2006};

    // Create a tow truck (Mater)
    TOWTRUCK towTruck = {"Mater", NULL};  // Initialize the towedCar pointer to NULL

    // Simulate towing Lightning McQueen
    towCar(&towTruck, &lightningMcQueen);

    // Access the towedCar pointer from the tow truck
    if (towTruck.towedCar != NULL) {
        printf("%s tow truck is currently towing a %d %s.\n", towTruck.name, towTruck.towedCar->year,
               towTruck.towedCar->name);
    } else {
        printf("%s tow truck is not currently towing any car.\n", towTruck.name);
    }

    return 0;
}
