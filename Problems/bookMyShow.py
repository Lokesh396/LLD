from enum import Enum
import threading
import uuid
import time
import random

class SeatStatus(Enum):

    AVAILABLE = 'AVAILABLE'
    HELD = 'HELD'
    BOOKED = 'BOOKED'


class Seat:
    def __init__(self, seat_id):
        self.seat_id = seat_id
        self.status = SeatStatus.AVAILABLE
    
    def is_available(self):
        return self.status == SeatStatus.AVAILABLE

    def set_status(self, status):
        self.status = status
    

class Show:

    def __init__(self, show_name, show_id, seat_ids):
        self.show_name = show_name
        self.show_id = show_id
        self.seats = {sid:Seat(sid) for sid in seat_ids}
        self._lock = threading.Lock()


class Booking:

    def __init__(self, user, seat_ids, show, booking_id):
        self.booking_id = booking_id
        self.show = show
        self.seat_ids = seat_ids
        self.user = user
        self.status = 'PENDING'
    
    def set_status(self, status):
        self.status = status

class BookingService:


    def reserve_seats(self, show, seat_ids, user):
        with show._lock:
            for sid in seat_ids:
                seat = show.seats[sid]
                if not seat.is_available():
                    return False
            
            for sid in seat_ids:
                seat = show.seats[sid]
                seat.set_status(SeatStatus.HELD)
            
            booking = Booking(user, seat_ids, show, f'#{uuid.uuid4()}')
            if self.confirm_booking(booking):
                for sid in seat_ids:
                    seat = show.seats[sid]
                    seat.set_status(SeatStatus.BOOKED)
                return booking
            else:
                for sid in seat_ids:
                    seat = show.seats[sid]
                    seat.set_status(SeatStatus.AVAILABLE)
                return False

    def confirm_booking(self, booking):
            time.sleep(random.randint(2, 6))
            booking.set_status('CONFIRMED')
            return True
    
    def cancel_booking(self, booking):
        booking.set_status('CANCELLED')
        return True


if __name__ == '__main__':
    show = Show('Inception', 's1', ['A1', 'A2', 'A3'])
    service = BookingService()
    N = 10
    barrier = threading.Barrier(N)
    # --- Scenario 1: many threads race for the SAME seat -> exactly one wins ---
    results = []
    results_lock = threading.Lock()          # guard the shared results list

    def attempt(user):
        barrier.wait()
        time.sleep(random.uniform(0, 0.001))
        booking = service.reserve_seats(show, ['A1'], user)
        with results_lock:
            results.append((user, 'WON' if booking else 'LOST'))

    threads = [threading.Thread(target=attempt, args=(f'user_{i}',)) for i in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(results)
    winners = [u for u, r in results if r == 'WON']
    print("Scenario 1: 10 users race for seat A1")
    print("  winners:", winners)
    print("  A1 final status:", show.seats['A1'].status.value)
    assert len(winners) == 1, "exactly one booker should win A1"
    print("  PASS: exactly one winner\n")

    # --- Scenario 2: all-or-nothing -> request includes an already-taken seat ---
    print("Scenario 2: book [A1, A2] when A1 is already taken")
    booking = service.reserve_seats(show, ['A1', 'A2'], 'late_user')
    print("  result:", 'WON' if booking else 'LOST (rejected)')
    print("  A2 status (must stay AVAILABLE):", show.seats['A2'].status.value)
    assert booking is False
    assert show.seats['A2'].is_available(), "A2 must not be partially reserved"
    print("  PASS: no partial booking")