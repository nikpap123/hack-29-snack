import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import StarRatingComponent from 'react-star-rating-component';

const useStyles = makeStyles(theme => ({
  root: {
    width: '100%',
    marginTop: theme.spacing(3),
    overflowX: 'auto',
  },
  table: {
    minWidth: 650,
  },
}));

function createData(name, calories, present, rating) {
  var available = present?'Yes':'No';
  return { name, calories, available, rating };
}

const rows = [
  createData('Vanilla stroopwafel',120, false, 4),
  createData('Cookies and cream stroopwafel', 120,  false, 1),
  createData('Lemon luna bars', 120, false, 2),
  createData('Peanut butter dark chocolate kind bar', 120, true, 4),
  createData('Fruit snacks', 120, true, 3),
];

export default function SimpleTable(props) {
  const classes = useStyles();

  return (
    <Paper className={classes.root}>
      <Table className={classes.table}>
        <TableHead>
          <TableRow>
            <TableCell>Snack</TableCell>
            <TableCell align="right">Calories (kcal) </TableCell>
            <TableCell align="right">Available?</TableCell>
            <TableCell align="right">Popularity</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map(row => (
            <TableRow key={row.name} onClick={() => props.clickAction(row.name)}>
              <TableCell component="th" scope="row">
                {row.name}
              </TableCell>
              <TableCell align="right">{row.calories}</TableCell>
              <TableCell align="right">{row.available}</TableCell>
              <TableCell align="right">
                <StarRatingComponent
                  name={row.name}
                  value={row.rating}
                  editing={false}
                />
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </Paper>
  );
}
