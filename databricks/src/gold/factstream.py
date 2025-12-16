import dlt

@dlt.table
def factstream_stg():
    df = spark.readStream.table('spotify_catalog.silver.factstreaming')
    return df

dlt.create_streaming_table(name='factstream')

dlt.create_auto_cdc_flow(
    target='factstream',
    source='factstream_stg',
    keys=['stream_id'],
    sequence_by='stream_timestamp',
    stored_as_scd_type= 1,
    once= False
)