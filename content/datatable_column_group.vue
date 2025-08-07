<DataTable :value="sales" tableStyle="min-width: 50rem">
    <ColumnGroup type="header">
        <Row>
            <Column header="Product" :rowspan="3" />
            <Column header="Sale Rate" :colspan="4" />
        </Row>
        <Row>
            <Column header="Sales" :colspan="2" />
            <Column header="Profits" :colspan="2" />
        </Row>
        <Row>
            <Column header="Last Year" sortable field="lastYearSale" />
            <Column header="This Year" sortable field="thisYearSale" />
            <Column header="Last Year" sortable field="lastYearProfit" />
            <Column header="This Year" sortable field="thisYearProfit" />
        </Row>
    </ColumnGroup>
    <Column field="product" />
    <Column field="lastYearSale">
        <template #body="slotProps"> {{ slotProps.data.lastYearSale }}% </template>
    </Column>
    <Column field="thisYearSale">
        <template #body="slotProps"> {{ slotProps.data.thisYearSale }}% </template>
    </Column>
    <Column field="lastYearProfit">
        <template #body="slotProps">
            {{ formatCurrency(slotProps.data.lastYearProfit) }}
        </template>
    </Column>
    <Column field="thisYearProfit">
        <template #body="slotProps">
            {{ formatCurrency(slotProps.data.thisYearProfit) }}
        </template>
    </Column>
    <ColumnGroup type="footer">
        <Row>
            <Column footer="Totals:" :colspan="3" footerStyle="text-align:right" />
            <Column :footer="lastYearTotal" />
            <Column :footer="thisYearTotal" />
        </Row>
    </ColumnGroup>
</DataTable>