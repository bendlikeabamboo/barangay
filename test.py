from barangay import barangay

# Get all regions
regions = list(barangay.keys())
print(f"Total regions: {len(regions)}")

# Get cities/municipalities in a region
ncr = barangay["National Capital Region (NCR)"]
ncr_cities = list(ncr.keys())
print(f"NCR cities: {len(ncr_cities)}")

# Get barangays in a city
manila = ncr["City of Manila"]
manila_municipalities = list(manila.keys())
print(f"Manila municipalities: {len(manila_municipalities)}")


# Access a specific barangay
barangay_128 = manila["Barangay 128"]
print(f"Barangay 128: {barangay_128}")
