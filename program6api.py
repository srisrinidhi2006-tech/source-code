def print_report(data, title="REPORT"):
    """
    Simple text formatter that takes a dictionary and prints a clean report.
    """
    print("=" * 60)
    print(f"{title:^60}")
    print("=" * 60)
    
    # Calculate max key length for alignment
    max_key_len = max(len(str(key)) for key in data.keys()) if data else 0
    max_key_len = max(max_key_len, 20)  # Minimum width
    
    for key, value in data.items():
        # Handle nested dictionaries
        if isinstance(value, dict):
            print(f"\n{key.upper()}:")
            for subkey, subvalue in value.items():
                print(f"   • {subkey:<{max_key_len-3}}: {subvalue}")
        elif isinstance(value, list):
            print(f"\n{key.upper()}:")
            for item in value:
                print(f"   • {item}")
        else:
            # Format the value nicely
            if isinstance(value, bool):
                value_str = "Yes" if value else "No"
            elif value is None:
                value_str = "N/A"
            else:
                value_str = str(value)
                
            print(f"{key:<{max_key_len}}: {value_str}")
            
    print("=" * 60)

# Sample structured data
sample_data = {
    "report_id": "RPT-20260526-001",
    "generated_on": "2026-05-26 13:01",
    "status": "Completed",
    "user": {
        "name": "Alice Johnson",
        "email": "alice@example.com",
        "active": True,
        "join_date": "2024-03-15"
    },
    "performance": {
        "total_tasks": 142,
        "completed": 138,
        "success_rate": "97.18%"
    },
    "tags": ["urgent", "finance", "q2-review"],
    "notes": "Quarterly performance review completed successfully."
}

# Run the formatter
print_report(sample_data, title="QUARTERLY PERFORMANCE REPORT")