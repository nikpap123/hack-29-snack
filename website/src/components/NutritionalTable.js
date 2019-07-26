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
    // minWidth: 400,
  },
}));

function createData(name, value) {
  return { name, value };
}

export default function NutritionalTable(props) {
  const classes = useStyles();

  var rows = []
  for (var key in props.nutrition[props.snack]) {
    var val = props.nutrition[props.snack][key];
    if (!isNaN(val)){
      if (['cholesterol', 'sodium', 'potassium'].includes(key))
        val += ' mg'
      else
        val += ' g'
    }
    rows.push({
      'name': key,
      'value': val
    })
  }
  
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
