import math

def calculate_projectile_motion(v, theta, g=9.81):
    theta_rad = math.radians(theta)
    Vy = v * math.sin(theta_rad)
    Vx = v * math.cos(theta_rad)
    
    time_of_flight = (2 * Vy) / g
    max_height = (Vy ** 2) / (2 * g)
    horizontal_range = Vx * time_of_flight
    
    return {
        "time_of_flight": time_of_flight,
        "max_height": max_height,
        "horizontal_range": horizontal_range
    }

if __name__ == "__main__":
    v = float(input("Enter initial velocity (m/s): "))
    theta = float(input("Enter launch angle (degrees): "))
    
    results = calculate_projectile_motion(v, theta)
    
    print("\n--- Projectile Motion Results ---")
    print("Initial Velocity:", v, "m/s")
    print("Launch Angle:", theta, "°")
    print("---------------------------------")
    print("Time of Flight:  ", round(results["time_of_flight"], 2), "seconds")
    print("Maximum Height:  ", round(results["max_height"], 2), "meters")
    print("Horizontal Range:", round(results["horizontal_range"], 2), "meters")