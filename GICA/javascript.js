function generateMemberID() {
    var MIDPrefix = 'GAIA';
    var MID = 0;

    // Get the last member ID number from the database.
    var lastMember = Member.objects.last();
    if (lastMember) {
        MID = lastMember.MID;
    }

    // Increment the member ID number.
    MID++;

    // Add the  member ID number prefix.
    MID = MIDPrefix + MID;

    // Set the member ID number field.
    $('#MID').val(MID);
}

$(document).ready(function() {
    $('#MID').click(function() {
        generateMemberID();
    });
});
