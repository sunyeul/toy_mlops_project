import polars as pl


def add_family_size(df: pl.DataFrame) -> pl.DataFrame:
    return df.with_columns((pl.col("SibSp") + pl.col("Parch")).alias("Family_Size"))


def encode_is_male(df: pl.DataFrame) -> pl.DataFrame:
    return df.with_columns(
        pl.when(pl.col("Sex") == "male").then(1).otherwise(0).alias("Is_Male")
    )


def preprocess_titanic_data(df: pl.DataFrame) -> pl.DataFrame:
    age_mean = df["Age"].mean()
    df = df.with_columns(
        pl.col("Age").fill_null(age_mean), pl.col("Embarked").fill_null("S")
    )

    df = add_family_size(df)
    df = encode_is_male(df)

    df = df.drop(["Name", "Ticket", "Cabin"])

    return df
