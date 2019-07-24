import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

const useStyles = makeStyles(theme => ({
  root: {
    width: '100%',
    marginTop: theme.spacing(3),
    overflowX: 'auto',
  },
  table: {
    minWidth: 400,
  },
}));

function createData(name, value) {
  return { name, value };
}

const rows = [
  createData('Calories (kcal)', 120),
  createData('Total Fat (g)', 6),
  createData('Cholesterol (mg)', 5),
  createData('Sodium (mg)', 90),
  createData('Total Carbohydrates (g)', 19),
  createData('Protein (g)', 1) 
];

export default function NutritionalTable(props) {
  const classes = useStyles();

  return (
    <Paper className={classes.root}>
      <Table className={classes.table}>
        <TableBody>
          {rows.map(row => (
            <TableRow key={row.name} >
              <TableCell component="th" scope="row">
                {row.name}
              </TableCell>
              <TableCell align="right">{row.value}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </Paper>
  );
}
