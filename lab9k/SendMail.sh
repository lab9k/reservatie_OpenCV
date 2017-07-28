#!/usr/bin/env bash
#arguments: $1: mailadress user, $2: name user, $3: datum, $4: zaal
if [ "$#" -ne 4 ] ; then
    echo "Number of arguments given: $#"
    echo "No mailaddress given"
    exit 1
fi


curl -s --user 'api:key-KEYHERE' \
    https://api.mailgun.net/v3/mail.lab9k.gent/messages \
    -F from='Postmaster <postmaster@mail.lab9k.gent>' \
    -F to="$1" \
    -F subject='Bevestiging reservatie' \
    -F text=$'Beste $2,\nU heeft zaal "$4" gereserveerd op "$3".\n\nMet vriendelijke groeten,\nLab9000'
