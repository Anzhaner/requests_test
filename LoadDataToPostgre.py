import psycopg2

conn = psycopg2.connect("host='localhost' port='5432' dbname='testdb' user='postgres' password='postgres'")

filesFolder = 'C:\\Users\\Anzhaner\\Desktop\\Python\\MyTest\\TestData\\'
requests_file = 'requests_test.csv'
engineers_file = 'engineers_test.csv'

cur = conn.cursor()

def engineers_table_create(filesFolder):
    # cur = conn.cursor()
    cur.execute("""
        CREATE TABLE engineers_test(
        Num integer PRIMARY KEY,
        Name text,
        RegType text,
        QualificationClass text,
        OfficialName text,
        Region text,
        Rating text,
        PublicKey text
    )
    """)

    with open(filesFolder + 'engineers_test.csv', 'r') as f:
        next(f)  # Skip the header row.
        cur.copy_expert("""COPY engineers_test FROM STDIN WITH (FORMAT CSV)""", f)

    conn.commit()

def request_table_create(filesFolder):

    cur.execute("""
        CREATE TABLE requests_test(
        Num integer PRIMARY KEY,
        CreationTime timestamp,
        PerformanceTime timestamp,
        CloseTime timestamp,
        CashSolution boolean,
        Name text,
        CloseReasonComment text,
        CloseCancelComment text,
        RequestNumber text,
        OfficialName text,
        DepartureOnRequest boolean,
        ServiceBranchCode text,
        ServiceCategory text,
        Region text,
        RequiredServices text,
        DirectiveRequest boolean,
        SerialNum text,
        WaitingReason text,
        CheckOutResult text,
        ActuallyPerformedServices text
    )
    """)

    with open(filesFolder + 'requests_test.csv', 'r') as f:
        next(f)  # Skip the header row.
        cur.copy_expert("""COPY requests_test FROM STDIN WITH (FORMAT CSV)""", f)

    conn.commit()

engineers_table_create(filesFolder)
request_table_create(filesFolder)

