# Spark Submit for `pyspark` using ZIP file

## Ikhtisar

Seluruh variabel konfigurasi runtime Spark Submit diletakkan di dalam script `run.sh`

Perintah `Spark Submit` yang digunakan:

```sh
#!/bin/bash

SPARK_PATH="/apps/hadoop/hdp/2.6.2.0-205/spark2/bin"

APP_NAME="[Spark App] Change this with your app name."
SPARK_MASTER="yarn"
SPARK_EXECUTOR_CORES="2"
SPARK_DRIVER_MEMORY="2g"
SPARK_EXECUTOR_MEMORY="2g"
SPARK_EXECUTOR_INSTANCES="2"

$SPARK_PATH/spark-submit \
	--master yarn \
	--deploy-mode cluster \
	--conf "spark.app.name=$APP_NAME" \
	--conf "spark.master=$SPARK_MASTER" \
	--conf "spark.executor.cores=$SPARK_EXECUTOR_CORES" \
	--conf "spark.driver.memory=$SPARK_DRIVER_MEMORY" \
	--conf "spark.executor.memory=$SPARK_EXECUTOR_MEMORY" \
	--conf "spark.executor.instances=$SPARK_EXECUTOR_INSTANCES" \
	--jars sqljdbc42.jar \
	--driver-class-path sqljdbc42.jar \
	--py-files src.zip \
    main.py
   
```

## Cara menjalankan

- Kopikan file berikut ke server:
  * `run.sh`
  * `main.py`
  * `src.zip`

- Jalankan script `run.sh`:

```./run.sh```

## TODO

- Integrasi dengan unit test
- Integrasi dengan dependensi (https://bytes.grubhub.com/managing-dependencies-and-artifacts-in-pyspark-7641aa89ddb7)
- Memindahkan parameter-parameter spark submit ke variabel shell script