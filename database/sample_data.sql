INSERT INTO loads (load_id, origin, destination, pickup_datetime, delivery_datetime, 
                  equipment_type, loadboard_rate, weight, commodity_type, num_of_pieces, 
                  miles, dimensions, notes) VALUES
('LD001234', 'Chicago, IL', 'Atlanta, GA', '2025-09-16 08:00:00', '2025-09-18 17:00:00', 
 'Dry Van', 2450.00, 25000, 'Electronics', 15, 715, '48x8.5x9', 'No touch freight'),
('LD001235', 'Los Angeles, CA', 'Phoenix, AZ', '2025-09-16 10:00:00', '2025-09-17 14:00:00', 
 'Flatbed', 1850.00, 35000, 'Construction Materials', 8, 370, '48x8.5x4', 'Tarps required'),
('LD001236', 'Miami, FL', 'New York, NY', '2025-09-17 06:00:00', '2025-09-19 23:59:00', 
 'Reefer', 3200.00, 28000, 'Produce', 1, 1285, '53x8.5x9', 'Keep at 34°F'),
('LD001237', 'Dallas, TX', 'Denver, CO', '2025-09-16 14:00:00', '2025-09-18 10:00:00', 
 'Dry Van', 1950.00, 22000, 'Retail Goods', 25, 781, '48x8.5x9', 'Appointment required');
