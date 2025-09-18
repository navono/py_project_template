import random

{%- if use_prefect %}
from prefect import flow, task


@task
def get_customer_ids() -> list[str]:
    # Fetch customer IDs from a database or API
    return [f"customer{n}" for n in random.choices(range(100), k=10)]


@task
def process_customer(customer_id: str) -> str:
    # Process a single customer
    return f"Processed {customer_id}"


@flow
async def process_flow():
    logger.info("Processing customers in flow")
    customer_ids = get_customer_ids()
    # Map the process_customer task across all customer IDs
    results = process_customer.map(customer_ids)
    return results
{%- else %}
# Prefect not enabled, using simple functions
{%- endif %}

from .utils import Config, CustomizeLogger

gen_config = Config().get_config()
logger = CustomizeLogger.make_logger(gen_config["log"])


async def start():
    logger.info("Hello from {{ project_name }}!")
    {%- if use_prefect %}
    # Run the flow
    results = await process_flow()
    {%- else %}
    # Simple processing without Prefect
    customer_ids = [f"customer{n}" for n in random.choices(range(100), k=10)]
    results = [f"Processed {customer_id}" for customer_id in customer_ids]
    logger.info(f"Processed {len(results)} customers")
    {%- endif %}
    return results