# my_module/notebook_runner.py

class NotebookRunner:
    def __init__(self, notebook_path, timeout_seconds=60, arguments=None):
        if arguments is None:
            arguments = {}
        self.notebook_path = notebook_path
        self.timeout_seconds = timeout_seconds
        self.arguments = arguments

    def get_dbutils(self):
        try:
            from pyspark.dbutils import DBUtils
            from pyspark.sql import SparkSession
            spark = SparkSession.builder.getOrCreate()
            return DBUtils(spark)
        except ImportError:
            raise ImportError("dbutils is not available. This code should be run inside a Databricks notebook.")

    def run_notebook(self):
        dbutils = self.get_dbutils()
        
        # Use dbutils to run the notebook and capture output
        output = dbutils.notebook.run(
            self.notebook_path,
            timeout_seconds=self.timeout_seconds,
            arguments=self.arguments
        )
        return output
