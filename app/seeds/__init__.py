from flask.cli import AppGroup
from .users import seed_users, undo_users
from .bookings import seed_bookings, undo_bookings
from .bookingsAmenities import seed_bookingsAmenities, undo_bookingsAmenities
from .states import seed_states, undo_states
from .pictures import seed_pictures, undo_pictures
from .reviews import seed_reviews, undo_reviews
from .amenities import seed_amenities, undo_amenities
from .reservations import seed_reservations, undo_reservations

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')

# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_states()
    seed_bookings()
    seed_pictures()
    seed_reviews()
    seed_reservations()

    # seed_amenities() #Combined into seeding_bookings
    # seed_bookingsAmenities()
    # Add other seed functions here

# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_reservations()
    undo_reviews()
    undo_pictures()
    undo_bookings()
    undo_states()
    undo_users()



    # undo_amenities()#combinded into seeding bookings
    # undo_bookingsAmenities()
    # Add other undo functions here
