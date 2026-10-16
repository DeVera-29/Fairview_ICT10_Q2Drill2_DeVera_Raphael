from pyscript import document, display

club_members = ["Tom Pearl", "Bill Urine", "Big goy", "John Feces", "Benjamin Juice", "Joe Montessori", "Tone Doe", "Pilly Pinas"]

grade7 = {"Tom Pearl", "John Feces"}
grade8 = {"Bill Urine", "Benjamin Juice"}
grade9 = {"Big goy", "Joe Montessori"}
grade10 = {"Tone Doe", "Pilly Pinas"}

def check_candidate(e):
    first_name = document.getElementById("fname").value.strip()
    last_name = document.getElementById("lname").value.strip()
    full_name = f"{first_name} {last_name}"
    is_member = full_name in club_members

    

    messages = [
        f"Sorry {full_name}, you are NOT on the list.",
        f"Congratulations {full_name}! You're' now in Rainbow Catering."
    ]

    result_message = messages[int(is_member)]

    # clear result and show new message
    document.getElementById("result").innerHTML = ""
    display(result_message, target="result")

    
    new_member_set = {full_name}
    Big_set = grade7 | grade8 | grade9 | grade10 | new_member_set

    formatted_members = ", ".join(sorted(Big_set))
    document.getElementById("members_box").innerHTML = ""
    display(f"Total Members: {len(Big_set)}", target="members_box")
    display(f"All Members: {formatted_members}", target="members_box")