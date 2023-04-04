import streamlit as st
from sqlalchemy import Column, Integer, Text, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class AnalysisResults(Base):
    __tablename__ = 'analysis_results'
    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    avg_max_temp = Column(Float)
    avg_min_temp = Column(Float)
    total_precipitation = Column(Float)

engine = create_engine('sqlite:///weather.db')
Session = sessionmaker(bind=engine)
session = Session()

def analysis_results_query():
    query = session.query(AnalysisResults)
    return query.all()

def main():
    st.set_page_config(page_title='Weather Data Analysis', page_icon=':partly_sunny:')
    st.title('Weather Data Analysis')

    engine = create_engine('sqlite:///weather.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    analysis_results = session.query(AnalysisResults).all()

    if not analysis_results:
        st.warning('No analysis results found')
    else:
        st.write(f'Total records: {len(analysis_results)}')
        for record in analysis_results:
            st.write({
                'year': record.year,
                'avg_max_temp': record.avg_max_temp,
                'avg_min_temp': record.avg_min_temp,
                'total_precipitation': record.total_precipitation
            })
    session.close()


if __name__ == '__main__':
    main()
