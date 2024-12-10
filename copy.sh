#!/bin/bash

# Define the range, increments, and excluded values
start_value=33
end_value=36
increment=0.25
excluded_values=(34 35)

# Function to check if a value is excluded
is_excluded() {
    local value=$1
    for excluded in "${excluded_values[@]}"; do
        if [[ $(printf "%.2f" $value) == $(printf "%.2f" $excluded) ]]; then
            return 0
        fi
    done
    return 1
}

# Create folders and copy files
current_value=$start_value
while (( $(echo "$current_value <= $end_value" | bc -l) )); do
    if ! is_excluded $current_value; then
        folder_name="propane_sba15_$(printf "%.2f" $current_value)"
        mkdir -p "$folder_name"
        cp job.sh "$folder_name/"
        cp t* "$folder_name/"
        cp pore.inp "$folder_name/"
        cp propane* "$folder_name/"
    fi
    current_value=$(echo "$current_value + $increment" | bc)
done

